function hello() {
    axios.post("http://localhost:8080/add", {
        b: document.getElementById('b').value,
        x1: document.getElementById('x1').value,
        y1: document.getElementById('y1').value,
        x2: document.getElementById('x2').value,
        y2: document.getElementById('y2').value
    })
    .then(function (response) {
	    console.log(response);
	    alert("result:" + response)
	})
	.catch(function (error) {
	    console.log("hi")
	    console.log(error);
	});
}

function lenstra() {
    let config = {
      headers: {
        'Content-Type': 'multipart/form-data',
      }
    }

    let data = {
      n: document.getElementById('n').value,
      limit: document.getElementById('limit').value
    }
    axios.post("http://localhost:8080/lenstra", data, config)
    .then(function (response) {
        alert(response);
    })
    .catch(function (error) {
        console.log(error);
    });
}

function togglePage(typeOperation) {
    allElem = document.querySelectorAll('.operations');
    for(var i = 0; i < allElem.length; i++){
        allElem[i].style.display = 'none';
    }
    document.getElementById(typeOperation).style.display = 'block';
}