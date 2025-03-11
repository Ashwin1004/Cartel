// Simulated Data Fetch Function
async function fetchData() {
    const query = document.getElementById('sqlQuery').value;

    if (!query.trim()) {
        alert("❌ Please enter a valid SQL query.");
        return;
    }

    // Example of a request sent to your backend (to be implemented in Flask)
    try {
        const response = await fetch('/api/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        const result = await response.json();

        if (!result.length) {
            alert("❌ No data found for the given query.");
        } else {
            alert("✅ Data fetched successfully! Check the map for details.");
        }

    } catch (error) {
        alert("❌ Error connecting to backend. Check your API.");
        console.error(error);
    }
}
