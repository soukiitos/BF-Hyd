document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('water-intake-form');
    const waterIntakeList = document.getElementById('water-intake-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const userId = parseFloat(document.getElementById('user-id').value);
        const amount = parseFloat(document.getElementById('amount').value);
        const date = document.getElementById('date').value;

        // Send a POST request to add water intake
        fetch('/water_intake', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: userId,
                amount: amount,
                date: date
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Display the new water intake entry
            const waterIntakeEntry = document.createElement('div');
            waterIntakeEntry.classList.add('water-intake-entry');
            waterIntakeEntry.innerHTML = `
                <p>User ID: ${data.water_intake.user_id}</p>
                <p>Amount: ${data.water_intake.amount}</p>
                <p>Date: ${data.water_intake.date}</p>
            `;
            waterIntakeList.appendChild(waterIntakeEntry);
        })
        .catch(error => console.error('Error:', error));
    });

    // Fetch and display existing water intake entries
    fetch('/water_intake/1') // Replace 1 with the actual user ID
    .then(response => response.json())
    .then(data => {
        data.forEach(entry => {
            const waterIntakeEntry = document.createElement('div');
            waterIntakeEntry.classList.add('water-intake-entry');
            waterIntakeEntry.innerHTML = `
                <p>User ID: ${entry.user_id}</p>
                <p>Amount: ${entry.amount}</p>
                <p>Date: ${entry.date}</p>
            `;
            waterIntakeList.appendChild(waterIntakeEntry);
        });
    })
    .catch(error => console.error('Error:', error));
});