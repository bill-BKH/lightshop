            function timer(element){
                job = setTimeout(() => {
                    document.querySelector('#result').innerHTML = ''
                    fetch("http://127.0.0.1:8000/search/",{
                    method : "POST",
                    body: JSON.stringify({
                        product_title : search_bar.value
                    }),
                    headers: {"X-CSRFToken": csrftoken }
                    })
                    .then((response)=> response.json())
                    .then((json) => (for (const property in json.data) {console.log(`${property}: ${object[property]}`)}))
                },1000);
            };