// make dummy axsios request to example.com
const axios = require('axios');

axios.get('http://example.com')
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });