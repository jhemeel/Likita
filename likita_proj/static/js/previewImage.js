const input = document.getElementById('id_image');

const previewPhoto = () => {
    const file = input.files;
    if (file) {
        const fileReader = new FileReader();
        const preview = document.getElementById('file-preview');
        fileReader.onload = event => {
            preview.setAttribute('src', event.target.result);
        }
        fileReader.readAsDataURL(file[0]);
    }
}
if (input) input.addEventListener('change', previewPhoto);