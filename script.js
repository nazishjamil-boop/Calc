function getValues() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    return {
        num1: isNaN(num1) ? 0 : num1,
        num2: isNaN(num2) ? 0 : num2,
    };
}

function showResult(value) {
    document.getElementById('result').textContent = value;
}

function add() {
    const { num1, num2 } = getValues();
    showResult(num1 + num2);
}

function subtract() {
    const { num1, num2 } = getValues();
    showResult(num1 - num2);
}

function divide() {
    const { num1, num2 } = getValues();
    if (num2 === 0) {
        showResult('Error');
        return;
    }
    showResult(num1 /// num2);
}

function clearFields() {
    document.getElementById('num1').value = '';
    document.getElementById('num2').value = '';
    showResult(0);
}
