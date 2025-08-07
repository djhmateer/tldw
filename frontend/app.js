// Document fetcher functionality
document.addEventListener('DOMContentLoaded', function() {
    const fetchBtn = document.getElementById('fetchDocumentBtn');
    const documentDisplay = document.getElementById('documentDisplay');
    const documentTitle = document.getElementById('documentTitle');
    const documentContent = document.getElementById('documentContent');
    const documentUpdated = document.getElementById('documentUpdated');

    fetchBtn.addEventListener('click', async function() {
        try {
            // Show loading state
            fetchBtn.textContent = 'Loading...';
            fetchBtn.disabled = true;

            // Fetch document data from the API
            const response = await fetch('/api/documents/44');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const document = await response.json();
            
            // Display the document data
            documentTitle.textContent = document.title;
            documentContent.textContent = document.content;
            documentUpdated.textContent = `Last updated: ${document.updated_at}`;
            
            // Show the display area
            documentDisplay.style.display = 'block';
            
            // Reset button
            fetchBtn.textContent = 'Fetch Document 44';
            fetchBtn.disabled = false;
            
        } catch (error) {
            console.error('Error fetching document:', error);
            
            // Display error message
            documentTitle.textContent = 'Error';
            documentContent.textContent = `Failed to fetch document: ${error.message}`;
            documentUpdated.textContent = '';
            documentDisplay.style.display = 'block';
            
            // Reset button
            fetchBtn.textContent = 'Fetch Document 44';
            fetchBtn.disabled = false;
        }
    });
}); 