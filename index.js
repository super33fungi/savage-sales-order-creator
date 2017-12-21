//Shopping Cart

inames = []
iqtyp = []
iprice = []

function addItem(productname){
  
  inames.push(productname)
  iqtyp.push(parseInt(document.getElementById('pqty').value))
  iprice.push(parseInt(document.getElementById('price').value))
  
  displayCart()
   
}

function displayCart(){
  
  
  cartdata = '<table><tr><th>Product Name</th><th>Quantity</th><th>Price</th><th>Total</th></tr>';
  
  total = 0;
  
  for (i=0; i<inames.length; i++){
    total += iqtyp[i] * iprice[i]
    cartdata += "<tr><td>" + inames[i] + "</td><td>" + iqtyp[i] + "</td><td>" + iprice[i] + "</td><td>" + iqtyp[i] * iprice[i] + "</td><td><button onclick='delElement(" + i + ")'>Delete</button></td></tr>"
  }
  
  cartdata += '<tr><td></td><td></td><td></td><td>' + total + '</td></tr></table>'
  
  document.getElementById('cart').innerHTML = cartdata
  
}

function delElement(a){
  inames.splice(a, 1);
  iqtyp.splice(a, 1)
  iprice.splice(a, 1)
  displayCart()
}
