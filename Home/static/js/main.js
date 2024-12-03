function createGauge(context, value, label) {
    new Chart(context, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [value, 100 - value],
                backgroundColor: ['#3e95cd', '#e0e0e0'],
                borderWidth: 0
            }],
            labels: [label]
        },
        options: {
            circumference: 180, // Thiết lập vòng tròn chỉ 180 độ
            rotation: 270, // Quay ngược lại vị trí phía trên
            cutout: '70%', // Tạo hiệu ứng đồng hồ
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                tooltip: {
                    enabled: false
                },
                legend: {
                    display: false
                }
            }
        }
    });
}


function fetchDataAndRenderGauges() {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/Apiv1/lastData", true);

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState === 4) {
            if (xhttp.status === 200) {
                try {
                    // Parse JSON response
                    const response = JSON.parse(xhttp.responseText);
                    console.log("API Response:", response);

                    // Lấy dữ liệu từ đối tượng JSON
                    const temperature = response.temperature ;
                    const humidity = response.humidity ;
                    const soilMoisture = response.soil_moisture ;
                    const waterLevel = response.water_level ;

                    // Render các biểu đồ Gauge
                    createGauge(document.getElementById('tempGauge').getContext('2d'), temperature, 'Temp');
                    createGauge(document.getElementById('humGauge').getContext('2d'), humidity, 'Hum');
                    createGauge(document.getElementById('waterLevelGauge').getContext('2d'), waterLevel, 'Water Level');
                    createGauge(document.getElementById('soilMoistureGauge').getContext('2d'), soilMoisture, 'Soil Moisture');
                    console.log(temperature)

                } catch (error) {
                    console.error("JSON parsing error:", error);
                }
            } else {
                console.error("API request failed. Status:", xhttp.status);
            }
        }
    };

    xhttp.send();
}

window.onload = fetchDataAndRenderGauges;
