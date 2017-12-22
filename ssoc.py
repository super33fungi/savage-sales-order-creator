import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""<html>    
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Savage Sales Order Creator</title>
        <meta name="Savage Sales Order Creator" content="An interactive Sales Order Creator for Savage Enterprises.">
		<script src="/index.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script type="text/javascript">
			function sticky_relocate() {
				var window_top = $(window).scrollTop();
				var div_top = $('#sticky-anchor').offset().top;
				if (window_top > div_top) {
				$('#sticky').addClass('stick');
				$('#sticky-anchor').height($('#sticky').outerHeight());
				} else {
				$('#sticky').removeClass('stick');
				$('#sticky-anchor').height(0);
				}
				}

				$(function() {
				$(window).scroll(sticky_relocate);
				sticky_relocate();
				});

				var dir = 1;
				var MIN_TOP = 200;
				var MAX_TOP = 350;

				function autoscroll() {
				var window_top = $(window).scrollTop() + dir;
				if (window_top >= MAX_TOP) {
				window_top = MAX_TOP;
				dir = -1;
				} else if (window_top <= MIN_TOP) {
				window_top = MIN_TOP;
				dir = 1;
				}
				$(window).scrollTop(window_top);
				window.setTimeout(autoscroll, 100);
			}
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
		</script>
		<style>
			#frm{
			  padding: 20px;
			  padding-right: 60px;
			  border: 2px solid;
			  display: inline-block;
			  height: 200px;
			  width: 200px;
			  margin: 10px 10px 10px 10px;
			  text-align: center;
			}

			#product-list {
			  list-style-type: none;
			}

			#product-button {
			  width:200px;
			  text-align: center;
			  margin-left: 20px;
			}

			#cart{
			  margin-top: 30px;
			  padding: 20px;
			  border: 2px solid;
			  background: #F5F5F5;
			  height: 90vh;
			  width:35%;
			  display: inline-block;
			  position: absolute;
			}

			th, td, tr{
			  border: 1px solid;
			}

			.product {
			  height: 350px;
			  width: 200px;
			  background-repeat: no-repeat;
			  background-position: center;
			  background-size: contain; 
			  display: inline-block;
			  margin: 10px 10px 10px 10px;
			  cursor: pointer;
			  text-align: center;
			}
			#product-input {
				position: relative;
				bottom: -220px;
			}
			#product-area {
			  width: 60%;
			  display: inline-block;
			}

			#product-button {
			  position: relative;
			  right: 20px;
			  bottom: -250px;
			}

			#sticky {
			  padding: 0.5ex;
			  width: 400px;
			  background-color: #333;
			  color: #fff;
			  font-size: 1.5em;
			  border-radius: 0.5ex;
			}

			#sticky.stick {
			  margin-top: 0 !important;
			  position: fixed;
			  top: 0;
			  z-index: 10000;
			  border-radius: 0 0 0.5em 0.5em;
			}

			#info-box {
			  font-size: 1.5em;
			  color: #fff;
			  background-color: #333;
			  padding: 0.5ex;
			  width: 300px;
			  border-radius: 0.5ex;
			  position: absolute;
			  top: 60px;
			  right: 40px;
			}

			body {
			  margin: 1em;
			  min-width: 1000px;
			  overflow: auto;
			}

			p {
			  margin: 1em auto;
			}
		</style>
        </head>
        <body style="background-color: gray; min-width: 1140px; position: relative;">
		<div><h1>Savage Sales Order Creator</h1><i style="position: absolute; top: -15px; right: -10px;">version 0.1</i></div>
			<div id="sticky-anchor"></div>
				<div id="sticky">
					<label>Set product price:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
						<input id='price' type='number'><br>
					<label>Set product Quantity:</label>
						<input id='pqty' type='number'>			
				</div>
				<div id="info-box">
					<label>Client:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
						<input type="text"><br>
					<label>Sales Rep:</label>
						<input type="text">
				</div>
                <div id="product-area">
                    <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/bond_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('Bond')">
                    <h2 class="item_name"> Bond </h2>
                </div>
                <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/CUNDERWOOD_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('C. Underwood')">
                    <h2 class="item_name"> C. Underwood </h2>
                </div>
                <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/CENA_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('Cena')">
                    <h2 class="item_name"> Cena </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/JACKMAN_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('Jackman')">
                    <h2 class="item_name"> Jackman </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/JB_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('JB')">
                    <h2 class="item_name"> JB </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/PINKMAN_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('Pinkman')">
                    <h2 class="item_name"> Pinkman </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/QUINN_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('Quinn')">
                    <h2 class="item_name"> Quinn </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/FUNDERWOOD_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('F. Underwood')">
                    <h2 class="item_name"> F. Underwood </h2>
                </div>
                 <div class="simpleCart_shelfItem product" style="background-image: url(https://cdn.shopify.com/s/files/1/2301/4289/products/WHITE_270x_crop_bottom.png); background-color: darkgray;" onclick="addItem('White')">
                    <h2 class="item_name"> White </h2>
                </div>
            </div>
            <div id="cart" style="background-color: #F5F5F5">
                <h2>Click on a product image to add.</h2>
            </div>
        </body>
</html>
""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("my_name")
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)