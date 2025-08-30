/* Program napiše funkcijo, ki vzame seznam in vrne povprečno vrednost
števila v seznamu (vsota vseh elementov deljena s številom vseh)
seznam = [1, 3, 5, 7, 9, 11, 13]
*/ 
function povprecje(seznam) {
    var sum = 0;
    for(var i = 0; i < seznam.length; i++) sum = sum + seznam [i];
    return sum / seznam.length;
}

s = prompt('Vpiši število za fibonacci')
s = parseInt(s)
function fibonacci(n) {
    if (n <= 1) return 1;
    return fibonacci(n - 1) + fibonacci(n-2);
}
console.log(fibonacci(s));