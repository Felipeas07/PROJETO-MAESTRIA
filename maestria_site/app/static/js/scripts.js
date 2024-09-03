document.getElementById('menu-toggle').addEventListener('click', function() {
    let sidebar = document.getElementById('sidebar');
    sidebar.style.left = (sidebar.style.left === '-250px' || sidebar.style.left === '') ? '0' : '-250px';
});

// Simulação de login
document.getElementById('login-form')?.addEventListener('submit', function(e) {
    e.preventDefault();
    localStorage.setItem('loggedIn', 'true');
    window.location.href = 'index.html';
});

document.getElementById('cadastro-form')?.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Cadastro realizado com sucesso!');
    window.location.href = 'login.html';
});

document.getElementById('logout-link')?.addEventListener('click', function() {
    localStorage.removeItem('loggedIn');
    window.location.href = 'logout.html';
});

window.onload = function() {
    let loggedIn = localStorage.getItem('loggedIn');
    if (loggedIn === 'true') {
        document.getElementById('login-link').style.display = 'none';
        document.getElementById('logout-link').style.display = 'block';
    } else {
        document.getElementById('login-link').style.display = 'block';
        document.getElementById('logout-link').style.display = 'none';
    }
};
