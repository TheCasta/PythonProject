export function dataToTable(tableID) {
    // Richiesta GET per ottenere i dati
    fetch('http://127.0.0.1:5000/data')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const tableElement = document.getElementById(tableID);
            tableElement.innerHTML = '';  // Pulire l'elemento prima di aggiungere nuovi dati
            data.forEach(task => {
                const taskElement = document.createElement('div');
                taskElement.innerText = `Title: ${task[1]}, Description: ${task[2]}, Due Date: ${task[3]}`;
                tableElement.appendChild(taskElement);
            });
        })
        .catch(error => console.error('Error:', error));

    // Dati da inviare con la richiesta POST
    const postData = {
        title: "Compito di esempio",
        description: "Questo è un compito di esempio",
        due_date: "2024-06-01"
    };

    // Richiesta POST per inviare i dati
    fetch('http://127.0.0.1:5000/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => console.log('Successo:', data))
    .catch(error => console.error('Errore:', error));
}
