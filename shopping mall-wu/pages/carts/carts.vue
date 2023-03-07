<template>
	<view>
		<view style="position: fixed;top: 0;width: 100%;z-index:9999">
			<view class="header bg-gradual-blue" >
				Shopping cart
			</view>
		</view>
		
		<view style="margin-top:100upx;" >
			<view v-for="(p,i) in carts" :key="i">
				<view style="padding:20upx 20upx 20upx 1upx;border-bottom: 1upx solid #e7e7e7;" class="flex justify-around bg-white">
					<view style="width: 300upx;">
						<image @click="gotodetail(carts[i].goods_id)" style="width: 180upx;height: 200upx;margin-left: 70upx;" :src="banners[i].image"></image>
					</view>
					<view style="width: 440upx; margin-top: 35upx;borflex-direction: column; ">
						<view style=" font-size: 110%;">
							{{banners[i].goods_name}}
							<view><button @click="removeCart(p.goods_id,userInfo.uid)" class="cu-btn round">remove</button></view>
						</view>
						
						<view class="flex justify-between">
							<view style="font-size: 130%;padding-top: 50upx;">
								<text style="color: #06618c;"><text style="font-size: 85%;">$</text>{{banners[i].price}}</text>
								
							</view>

							<view class="flex" style="font-size: 130%;padding-top: 3upx;">
								
								<button @click="minusOne(p.goods_id,userInfo.uid)" class="cu-btn">-</button>
								<view><button @click="" class="cu-btn round bg-white">{{p.quantity}}</button></view>
								<button @click="addOne(p.goods_id,userInfo.uid)" class="cu-btn"><view>+</view></button>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<!--total-->
		<view class="total flex justify-between align-center">
			<view style="font-size: 110%;color:#747373;"> <text style="padding-left: 10upx; font-family: monospace; font-size: 100%;">Subtotal: {{sumdata[0].sum2}}|| Quantity: {{sumdata[0].sum1}}</text></view>
			<view>
				<view v-if="banners.length>0" @click="checkoutCart()" class="cu-btn bg-gradual-blue round" >Checkout</view>
			</view>
		</view>
	</view>
</template>

<script>
	import uniNumberBox from "@/components/uni-number-box/uni-number-box.vue"
	export default {
		data() {
			return {
				lists:[],
				carts:[],
				banners:[],
				customer_id:"",
				user_id:"",
				userIsLogin:false,
				userInfo:"",
				order_id:"",
				smachine:0,
				sumdata:[],
			}
		},
		components:{uniNumberBox},
		
		computed: {
			sum(){
				var s=0
				this.lists.forEach(p=>{
					if(p.checked==true){
						s+=p.num*p.price
					}
				})
				return s.toFixed(2);
			}
		},
		
		methods: {
			
			onLoad(){
				var userInfo = this.getGlobalUser("globalUser")
				if(userInfo!=null){
					this.userIsLogin = true;
					this.userInfo = userInfo;
				}else{
					this.userIsLogin = false;
					this.userInfo = {};
				}
				
				//console.log("uid:"+this.userInfo.uid)
				
				this.getcart(this.userInfo.uid)
				
				console.log("smachine")
				
				// if(this.smachine==1){
				// 	console.log("smachine")
				// 	location.reload()
				// 	this.smachine=1
				// }
			},
			
			gotodetail(id) {
				
				console.log(id)
				uni.navigateTo({
					url:`../gooddetail/gooddetail?id=${id}`//填货物id
				})
			},
			
			getcart(input){
				uni.request({
					url:`http://127.0.0.1:4444/user/cart?id=${input}`,
					data:{
						
					},
					success:(res) =>{
						this.carts=res.data.data
						this.banners=res.data.banners
						
						this.sumdata=res.data.sumdata
						console.log(this.carts)
						console.log(this.banners)
					}					
				})
			},
			
			

			addOne(input1,input2){
				//console.log(input1)
				//console.log(input2)
				uni.request({
					url:`http://127.0.0.1:4444/cart/add_quantity?id=${input1}&uid=${input2}`
				})
				location.reload()
			},
			
			minusOne(input1,input2){
				//console.log(input1)
				//console.log(input2)
				uni.request({
					url:`http://127.0.0.1:4444/cart/minus_quantity?id=${input1}&uid=${input2}`
				})
				location.reload()
			},
			removeCart(input1,input2){
				//console.log(input1)
				//console.log(input2)
				uni.request({
					url:`http://127.0.0.1:4444/goods/removecart?id=${input1}&uid=${input2}`
				})
				location.reload()
			},
			checkoutCart(){
				console.log(this.userInfo.uid)
				
				/*uni.request({
					url:`http://127.0.0.1:4444/cart/checkout?id=${this.userInfo.uid}`,
				})*/
								
				uni.request({
					url: `http://127.0.0.1:4444/cart/checkoutdetail?id=${this.userInfo.uid}`,
					data:{
						
					},
					success:(res) =>{
						this.order_id=res.data.order[0].order_id;
						console.log(this.order_id)
						uni.navigateTo({
							url:`../orderdetail/orderdetail?id=${this.order_id}`
						})
					},
					
					
					
				})
				
				
				
				
				
			},

		}
	}
</script>

<style>
	
.header{
	text-align: left;
	font-size: 170%;
	background-color: white;
	font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	padding-left: 20upx;
	border-bottom: 1upx solid #e7e7e7;
	padding-top: 20upx;
	padding-bottom: 20upx;
}
	
.operate{
	background-color: white;
	display: flex;
	height: 80upx;
	align-items: center;
	width: 750upx;
	padding-left: 30upx;
	padding-right: 0upx;
	border-bottom: 1upx solid #e7e7e7
}

.total{
	position: fixed;
	bottom: 90upx;
	width: 750upx;
	height: 100upx;
	background-color: white;
	padding-left: 30upx;
	padding-right: 20upx;
}

.cart-content{
	margin-top: 170upx;
	margin-bottom: 1200upx;
	height: 0;
}

.cart-item{
	display: flex;
	justify-content: space-between;
	padding: 20upx 20upx 20upx 20upx;
	margin-top:1upx;
}

.cart-item image {
	width: 180upx;
	height: 240upx;
	padding-left: 8upx;
}

.cart-item checkbox{
	margin-left: 20upx;
}

.cart-title{
	font-size: 110%;
	padding-top: 30upx;
	overflow: hidden;
}

.cart-ycontent{
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	padding-top: 8upx;
	
	padding-bottom: 8upx;
	margin-bottom: 20upx;
}

.operationalButton{
	font-size: 25px;
	padding: 0upx 0;
	text-align: center;
	color: red;
	/*width: 90upx;
	height: 80upx;*/
}

</style>
