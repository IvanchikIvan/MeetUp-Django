let modal_account = document.getElementsByClassName('account-modal')[0]
let account_btn = document.getElementById('account')

let isOpenAccountModal = false

account_btn.addEventListener("click", function() {
    isOpenAccountModal ? modal_account.style.display = 'none' : modal_account.style.display = 'block'
    isOpenAccountModal = !isOpenAccountModal
})