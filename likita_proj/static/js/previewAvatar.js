const avatar = document.querySelector('input#id_avatar');

const previewAvatar = () => {
    const file = avatar.files;
    if (file) {
        const fileReader = new FileReader();
        const preview = document.getElementById('avatar-preview');
        fileReader.onload = event => {
            preview.setAttribute('src', event.target.result);
        }
        fileReader.readAsDataURL(file[0]);
    }
}
avatar.addEventListener('change', previewAvatar);