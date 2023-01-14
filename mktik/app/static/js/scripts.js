const clickButton = document.querySelector('#get-data')
const resultBlock = document.querySelector('#resp')


clickButton.addEventListener("click", () => {
const promise = getRemoteData();
promise.then(onDataReceive)
});


function onDataReceive(array){
    const result = document.querySelector('#resp');
    let dhcp_lease_resp = 0;
    result.innerHTML = "";
    array.forEach(element => {
        const li =document.createElement('li');
        li.innerHTML = JSON.stringify(element);
        result.appendChild(li);

    });

    array.forEach(element => {
        const li =document.createElement('li');
        getDhcpLeases(element.address).then(res => {
        dhcp_lease_resp = res[0]['host-name'];
        li.innerHTML = "id: " + element.id + ", IP addr: " + element.address + ", host: " + dhcp_lease_resp + ", comment:"+ element.comment;
        result.appendChild(li);
        }).catch( err => {
         li.innerHTML = "id: " + element.id + ", IP addr: " + element.address + ", host: " + err + ", comment:"+ element.comment;
         });



    });

}

function getRemoteData(){
const promise = axios.get('http://127.0.0.1:8000/addr_lst');

return promise.then((response) => {
    return response.data.message;
})
 .catch(function (error) {
    // handle error
    alert(error.message)
  });
}

function getDhcpLeases(filter_address){
  const promise = axios.get(`http://127.0.0.1:8000/dhcp_leases?filter_address=${filter_address}`);
  
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

