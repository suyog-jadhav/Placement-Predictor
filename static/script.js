document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect form data
    const formData = {
        CGPA: parseFloat(document.getElementById('cgpa').value),
        Internships: parseInt(document.getElementById('internships').value),
        Projects: parseInt(document.getElementById('projects').value),
        Workshops_Certifications: parseInt(document.getElementById('workshops').value),
        AptitudeTestScore: parseInt(document.getElementById('aptitude').value),
        SoftSkillsRating: parseFloat(document.getElementById('softSkills').value),
        ExtracurricularActivities: document.getElementById('extracurricular').value,
        PlacementTraining: document.getElementById('training').value,
        SSC_Marks: parseInt(document.getElementById('ssc').value),
        HSC_Marks: parseInt(document.getElementById('hsc').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        
        const resultDiv = document.getElementById('result');
        const predictionText = document.getElementById('prediction-text');
        const predictionScore = document.getElementById('prediction-score');
        
        resultDiv.classList.remove('hidden');
        
        if (result.error) {
            resultDiv.classList.remove('success', 'warning');
            resultDiv.classList.add('error');
            predictionText.textContent = `Error: ${result.error}`;
            predictionScore.textContent = '';
        } else {
            const probability = (result.probability * 100).toFixed(2);
            resultDiv.classList.remove('error');
            
            if (probability < 50) {
                resultDiv.classList.remove('success');
                resultDiv.classList.add('warning');
                predictionText.textContent = "Need significant improvement in key areas";
            } else {
                resultDiv.classList.remove('warning');
                resultDiv.classList.add('success');
                predictionText.textContent = probability >= 75 
                    ? "Excellent chances of placement!" 
                    : "Good chances of placement";
            }
            
            predictionScore.textContent = `Placement: ${probability}%`;
        }

    } catch (error) {
        console.error('Error:', error);
        const resultDiv = document.getElementById('result');
        const predictionText = document.getElementById('prediction-text');
        
        resultDiv.classList.remove('hidden');
        resultDiv.classList.add('error');
        predictionText.textContent = 'An error occurred while making the prediction.';
    }
});