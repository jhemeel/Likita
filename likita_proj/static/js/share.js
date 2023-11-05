const share = document.querySelector('.share')
let socialShareIcon = document.querySelector('.social-share-icons')

const handleShare = () => {
    if (share){
       share.addEventListener('click', () => {
            socialShareIcon.classList.toggle('social-visible')
            if (socialShareIcon.classList.contains('social-visible')){
                socialShareIcon.style.display = "flex"
                share.style.width = '500px' 
                share.style.textAlign = "left"
                share.style.paddingLeft = "2rem"
            }
            else{
                socialShareIcon.style.display = "none"
                share.style.width = '150px'
            }
            
       })
       
    }

    if (share){
        share.removeEventListener('click', () => {
            socialShareIcon.classList.toggle('social-visible')
            if (socialShareIcon.classList.contains('social-visible')){
                socialShareIcon.style.display = "flex"
                share.style.width = '350px' 
            }
            else{
                socialShareIcon.style.display = "none"
                share.style.width = '150px'
            }
            
       })
    }
}
handleShare()