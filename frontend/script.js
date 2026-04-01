const BASE_URL = "http://localhost:8000"; 

// 1. Array to hold the "Basket" of files before uploading
let filesToUpload = [];

/**
 * Event Listener: Handles file selection
 * This allows adding files one-by-one without overwriting the previous ones.
 */
document.getElementById('fileInput').addEventListener('change', function(e) {
    const newlySelectedFiles = Array.from(e.target.files);
    
    newlySelectedFiles.forEach(file => {
        // Only add if the file isn't already in our list (to prevent duplicates)
        const isDuplicate = filesToUpload.some(f => f.name === file.name && f.size === file.size);
        if (!isDuplicate) {
            filesToUpload.push(file);
        }
    });

    // Reset the actual input value so the change event triggers even if the same file is picked
    e.target.value = "";
    
    renderFileList();
});

/**
 * UI Helper: Renders the list of selected files with a remove button
 */
function renderFileList() {
    const display = document.getElementById("fileListDisplay");
    if (!display) return; // Ensure the div exists in your HTML

    if (filesToUpload.length === 0) {
        display.innerHTML = "<p style='color: gray;'>No files selected.</p>";
        return;
    }

    display.innerHTML = filesToUpload.map((file, index) => `
        <div style="background: #f8f9fa; padding: 8px; margin-bottom: 5px; border-radius: 5px; display: flex; justify-content: space-between; align-items: center; border: 1px solid #ddd;">
            <span>📄 ${file.name} (${(file.size / 1024).toFixed(1)} KB)</span>
            <button onclick="removeFile(${index})" style="width: auto; padding: 2px 8px; background: #dc3545; margin: 0;">✕</button>
        </div>
    `).join('');
}

/**
 * UI Helper: Removes a specific file from the basket
 */
function removeFile(index) {
    filesToUpload.splice(index, 1);
    renderFileList();
}

/**
 * ACTION: Uploads all files in the basket to the backend
 */
async function uploadFile() {
    const status = document.getElementById("uploadStatus");

    if (filesToUpload.length === 0) {
        status.innerText = "⚠️ Please select at least one file.";
        return;
    }

    let formData = new FormData();
    // Use the key "files" (plural) to match the FastAPI list[UploadFile] argument
    filesToUpload.forEach(file => {
        formData.append("files", file); 
    });

    status.innerText = "🚀 Uploading " + filesToUpload.length + " file(s)...";

    try {
        const res = await fetch(`${BASE_URL}/upload`, {
            method: "POST",
            body: formData
        });

        if (!res.ok) throw new Error("Server responded with error");

        const data = await res.json();
        status.innerText = "✅ Successfully processed " + data.documents_count + " data points!";
        
        // Optional: Clear the list after successful upload so user starts fresh
        // filesToUpload = [];
        // renderFileList();

    } catch (err) {
        status.innerText = "❌ Upload failed. Check if backend is running.";
        console.error(err);
    }
}

/**
 * ACTION: Sends the question to the Agent
 */
async function askQuestion() {
    const questionInput = document.getElementById("questionInput");
    const responseBox = document.getElementById("responseBox");
    const stepsBox = document.getElementById("agentSteps");
    const question = questionInput.value.trim();

    if (!question) {
        responseBox.innerText = "Please enter a question.";
        return;
    }

    responseBox.innerText = "🤖 Thinking...";
    stepsBox.innerText = "";

    try {
        const res = await fetch(`${BASE_URL}/query`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await res.json();

        responseBox.innerText = data.answer;
        stepsBox.innerHTML = `
            <hr>
            <p><strong>🧠 Plan:</strong> ${data.plan}</p>
            <p><strong>🔧 Tool:</strong> ${data.tool}</p>
            <p><strong>🔍 Context Preview:</strong> <small>${data.retrieved}...</small></p>
        `;
        
        // Clear question box for the next query
        questionInput.value = "";

    } catch (err) {
        responseBox.innerText = "❌ Error getting response from Agent.";
        console.error(err);
    }
}

function clearSession() {
    console.log("Clear button clicked!"); // Check your F12 console for this!
    
    // 1. Reset the internal array
    filesToUpload = [];
    
    // 2. Clear the UI displays
    const fileList = document.getElementById("fileListDisplay");
    if (fileList) fileList.innerHTML = "";

    const status = document.getElementById("uploadStatus");
    if (status) status.innerText = "Cleared.";

    const response = document.getElementById("responseBox");
    if (response) response.innerText = "Your answer will appear here...";

    const steps = document.getElementById("agentSteps");
    if (steps) steps.innerText = "";

    const qInput = document.getElementById("questionInput");
    if (qInput) qInput.value = "";

    const fInput = document.getElementById("fileInput");
    if (fInput) fInput.value = "";

    // 3. Optional: Tell the backend to wipe memory too
    fetch(`${BASE_URL}/clear-data`, { method: "POST" })
        .then(() => console.log("Backend cleared"))
        .catch(() => console.log("Backend clear route not found - skipping."));
}