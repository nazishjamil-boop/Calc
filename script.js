const API_URL = 'http://localhost:5000/calculate';

function getValues() {
    const num1 = parseFloat(document.getElementById('num1').value) || 0;
    const num2 = parseFloat(document.getElementById('num2').value) || 0;
    return { num1, num2 };
}

function showResult(value) {
    document.getElementById('result').textContent = value;
}

async function calculate(operation) {
    const { num1, num2 } = getValues();
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operation, num1, num2 })
        });
        const data = await response.json();
        showResult(data.error ? data.error : data.result);
    } catch {
        showResult('Server offline');
    }
}

function add()        { calculate('add'); }
function subtract()   { calculate('subtract'); }
function multiply()   { calculate('multiply'); }
function divide()     { calculate('divide'); }
function modulo()     { calculate('modulo'); }
function power()      { calculate('power'); }
function squareRoot() { calculate('sqrt'); }

function clearFields() {
    document.getElementById('num1').value = '';
    document.getElementById('num2').value = '';
    showResult(0);
}
