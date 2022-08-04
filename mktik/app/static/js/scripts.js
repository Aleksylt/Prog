const clickButton = document.querySelector('#get-data')
const resultBlock = document.querySelector('#resp')


clickButton.addEventListener("click", () => {
const promise = getRemoteData();
promise.then(onDataReceive)
});


function onDataReceive(array){
    const result = document.querySelector('#resp');
    result.innerHTML = "";
    array.forEach(element => {
        const li =document.createElement('li');
        li.innerHTML = JSON.stringify(element);
        result.appendChild(li);

    });

    array.forEach(element => {
        const li =document.createElement('li');
        li.innerHTML = "id: " + element.id + ", IP address: " + element.address + ", comment:"+ element.comment;
        result.appendChild(li);

    });


// для одного элемента
/*  const li =document.createElement('li');
        li.innerHTML = array.data.email
        document.querySelector('#resp').appendChild(li)
 */
}

function getRemoteData(){
//const promise = axios.get('https://reqres.in/api/users?page=2');
const promise = axios.get('http://127.0.0.1:8000/addr_lst');

return promise.then((response) => {
    return response.data.message;
})
 .catch(function (error) {
    // handle error
    alert(error.message)
  });
}



/*
// Make a request for a user with a given ID
axios.get('https://reqres.in/api/users/2')
  .then(function (response) {
    // handle success
 //   document.querySelector('#resp').append(data.data.email);
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

*/

