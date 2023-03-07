<template>
	<view>
		<view style="position: fixed;top: 0;width: 100%;z-index:9999;">
			<view @tap="gotomy()" class="header bg-gradual-blue">< Order Page </view> <!--operate-->
			</view>
			
					<view class="flex justify-between" style="margin-top:27upx;background-color: #f4f4f4;border-bottom: 1upx solid #e7e7e7;">
						<view style="padding-bottom:20upx;margin-left: 30upx;font-size: 120%;color: #6fb135;">current</view>
						
						<view @click="gotopast" style="padding-bottom:20upx;font-size: 120%;color:#06618c;">past</view>
						
						<view @click="gotoorder" style="padding-bottom:20upx;margin-right: 30upx;font-size: 120%;color:#06618c;">all</view>
					</view>
					
					<view style="margin-top:0upx;">
						<view v-for="(p,i) in orders" :key="i">
							<view  style="padding:20upx 20upx 20upx 1upx;border-bottom: 1upx solid #e7e7e7;" class="flex justify-around bg-white">
								<view @click="gotoorderdetail(orders[i].order_id)" style="width: 300upx;">
									<image style="width: 180upx;height: 200upx;margin-left: 70upx;" :src="orders[i].image"></image>
								</view>
								<view style="width: 440upx; margin-top: 35upx;borflex-direction: column; ">
									<view @click="gotoorderdetail(orders[i].order_id)" style=" font-size: 110%;">
										Order ID: {{orders[i].order_id}} Time: {{orders[i].order_date}}
									</view>
									
									<view class="flex justify-between">
										<view style="font-size: 130%;padding-top: 50upx;">
											<text style="color: #06618c;"><text style="font-size: 85%;">All {{orders[i].quantity}} goods</text></text>
										</view>
										<view style="font-size: 130%;padding-top: 50upx;">
											<text style="color: #06618c;"><text style="font-size: 85%;">|  {{getStatus(orders[i].status)}}</text></text>
										</view>
										<button @click="changeStatus3(orders[i].order_id)" v-if="orders[i].status==0||orders[i].status==1" class="flex bg-gradual-orange" style="font-size: 130%;padding-top: 3upx; height: 80upx;">
											cancel
										</button>
									</view>
								</view>
							</view>
						</view>
					
					
			</view>			
		</view>
</template>

<script>
	import uniNumberBox from "@/components/uni-number-box/uni-number-box.vue"
	export default {
		data() {
			return {
				orders:[],
				customer_id:"",
				user_id:"",
				userIsLogin:false,
				userInfo:"",
			}
		},
		components: {
			uniNumberBox
		},

		computed: {

		},

		methods: {
			
			getStatus(statusNumber){
				if(statusNumber==0){return "Pending"}
				if(statusNumber==1){return "Hold"}
				if(statusNumber==2){return "Shipped"}
				if(statusNumber==3){return "Cancelled"}
				return "error"
			},
			
			changeStatus3(input){
				uni.request({
					url:`http://127.0.0.1:4444/orders/changestatus3?id=${input}`,
				})
				location.reload()
			},
			
			gotoorderdetail(input) {
				
				console.log(input)
				uni.navigateTo({
					url:`../orderdetail/orderdetail?id=${input}`
				})
			},
			
			gotoorder(){
				uni.navigateTo({
					url:"./order"
				})
			},
			
			gotopast(){
				uni.navigateTo({
					url:"./order_past"
				})
			},

			onLoad(options) {
				var userInfo = this.getGlobalUser("globalUser")
				if(userInfo!=null){
					this.userIsLogin = true;
					this.userInfo = userInfo;
				}else{
					this.userIsLogin = false;
					this.userInfo = {};
				}
				
				console.log(this.userInfo.uid)
				this.getdata();
			},
			
			getdata() {
				uni.request({
					url:"http://127.0.0.1:4444/orders/current",
					data: {
						id:this.userInfo.uid
					},
					method:"GET",
					success: (res) => {
						this.orders=res.data.orders;
						//console.log(res.data.orders);
						
						console.log("orders:")
						console.log(this.orders)
						console.log("tt")
					}
				})
			},

			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
			},
		}
	}
</script>

<style>
	.header {
		text-align: left;
		font-size: 170%;
		background-color: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		padding-left: 20upx;
		border-bottom: 1upx solid #e7e7e7;
		padding-top: 20upx;
		padding-bottom: 20upx;
	}

	.operate {
		background-color: white;
		display: flex;
		height: 80upx;
		align-items: center;
		width: 750upx;
		padding-left: 30upx;
		padding-right: 0upx;
		border-bottom: 1upx solid #e7e7e7
	}

	.total {
		position: fixed;
		bottom: 90upx;
		width: 750upx;
		height: 100upx;
		background-color: white;
		padding-left: 30upx;
		padding-right: 20upx;
	}

	.cart-content {
		margin-top: 170upx;
		margin-bottom: 1200upx;
		height: 0;
	}

	.cart-item {
		display: flex;
		justify-content: space-between;
		padding: 20upx 20upx 20upx 20upx;
		margin-top: 1upx;
	}

	.cart-item image {
		width: 180upx;
		height: 240upx;
		padding-left: 8upx;
	}

	.cart-item checkbox {
		margin-left: 20upx;
	}

	.cart-title {
		font-size: 110%;
		padding-top: 30upx;
		overflow: hidden;
	}

	.cart-ycontent {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding-top: 8upx;

		padding-bottom: 8upx;
		margin-bottom: 20upx;
	}

	.numberOfItems {
		width: 120upx;
		background-color: #EBEEF5;
		color: #000000;
		padding: 40upx 0;
		text-align: center;
		border-radius: 22rpx;
		font-size: 12upx;
	}

	.status {
		font-size: 8upx;
		padding: 15upx 0;
		text-align: center;
		color: #0081FF;
	}

	.cancelButton {
		font-size: 5px;
		padding: 0upx 0;
		text-align: center;
		color: white;
		width: 90upx;
	}
</style>
