var updatebtn = document.getElementsByClassName('update-cart')
for (var i = 0; i < updatebtn.length; i++) {
    updatebtn[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        updateOrder(productId, action)
    })
}

function updateOrder(productId, action) {
    console.log('User is logged in, sending data.....');
    var url = '/checkout/update_item/'
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
                // location.reload()
        })

}