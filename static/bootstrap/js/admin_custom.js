document.addEventListener('DOMContentLoaded', function() {
    const firstNameInput = document.querySelector('#id_first_name');
    const apPaternoInput = document.querySelector('#id_ap_paterno');
    const apMaternoInput = document.querySelector('#id_ap_materno');
    const usernameInput = document.querySelector('#id_username');

    function generateUsername() {
        const firstName = firstNameInput.value.toLowerCase();
        const apPaterno = apPaternoInput.value.toLowerCase();
        const apMaterno = apMaternoInput.value.toLowerCase();
        if (firstName && apPaterno && apMaterno) {
            usernameInput.value = `${firstName}.${apPaterno}.${apMaterno}`;
        }
    }

    firstNameInput.addEventListener('input', generateUsername);
    apPaternoInput.addEventListener('input', generateUsername);
    apMaternoInput.addEventListener('input', generateUsername);
});