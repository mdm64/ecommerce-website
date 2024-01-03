var updateBtns = document.getElementsByClassName('update-cart')

for (i=0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productID, 'action:', action)

        console.log('user', user)
        if(user == 'AnonymousUser'){
            console.log("not logged in")
        }
        else{
            updateUserOrder(productID, action) 
        }
    })
}
function updateUserOrder(productID, action) {
    console.log('User is authenticated, sending data')

    var url = '/updateItem/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productID':productID, 'action':action})
    })

    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    });
}
// the only way to send information here like about user and all we need to pass tha through main.html like request.user
    // <script type="text/javascript">
    //             var user = '{{request.user}}'
    // </script>
    // add this in main.html at top

    // we need to create a url path and send the above data on the view using jsonresponse
    // now we'll create updateUserOrder function in js file and send the data to the url we just created in views
    // u need to add csrf token as ajax and include it in main.html along side the user variable
    // now we have successfuly send the data to the url now we can load this data in view.py using read json method