<template>
	<view>
		<view style="position: fixed;top: 0;width: 100%;z-index:9999;">
			<view @tap="gotoorder()" class="header bg-gradual-blue">
				< Order Detail Page 
			</view>			
		</view>
		
		<view style="height: 230upx; background-color: #ffffff; margin-top: 15upx;padding-left: 15upx; color: #007AFF;">
			<view>
				Address:{{userInfo.uAddress}}
			</view>
			<view>
				User: {{userInfo.uName}}
			</view>
			<view>
				Order ID:{{goodsInOrder[0].order_id}}
			</view>
			<view>
				Total Amount: {{orders[0].amount}}
			</view>
			<view>
				Total Amount: {{getStatus(orders[0].status)}}
			</view>
			<view>
				Order Created Time: {{orders[0].order_date}}
			</view>
			<view v-if="orders[0].status==2">
				Shipped date: {{orders[0].shipped_date}}
			</view>
			<view v-if="orders[0].status!=2">
				Shipped date: null
			</view>
		</view>
		
		<view style="margin-top:10upx;">
			<view v-for="(p,i) in goodsInOrder" :key="i">				
				<view @tap="gotodetail(p.goods_id)" style="padding:20upx 20upx 20upx 1upx;border-bottom: 1upx solid #e7e7e7;" class="flex justify-around bg-white">
					<view style="width: 300upx;">
						<image style="width: 180upx;height: 200upx;margin-left: 70upx;" :src="banners[i].image"></image>
					</view>
					<view style="width: 440upx; margin-top: 35upx;borflex-direction: column; ">
						<view>
							{{banners[i].goods_name}}
						</view>
						<view style="font-size: 130%;padding-top: 10upx;">
							<text style="color: #06618c;"><text style="font-size: 85%;">$</text>{{p.goods_price}}</text>
						</view>
						<view style="padding-top: 10upx;">
							<text style="color: #06618c;"><text style="font-size: 55%;">X</text>{{p.goods_quantity}} Total Price: ${{p.goods_quantity*p.goods_price}}</text>
						</view>
					</view>
				</view>
				
				
			</view>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				goodsInOrder : [],
				banners:[],
				order_id:"",
				userInfo:"",
				orders:[],
			}
		},
		onShow(){
			var userInfo = this.getGlobalUser("globalUser")
			if(userInfo!=null){
				this.userIsLogin = true;
				this.userInfo = userInfo;
			}else{
				this.userIsLogin = false;
				this.userInfo = {};
			}
			
		},
		methods: {
			getdata() {
				uni.request({
					url:"http://127.0.0.1:4444/orders/orderdetail",
					data: {
						id:this.order_id
					},
					method:"GET",
					success: (res) => {
						this.goodsInOrder = res.data.detail;
						this.banners = res.data.banners;
						this.orders=res.data.result;
						//console.log(res.data.detail); 
						console.log(this.orders);
						console.log(this.goodsInOrder);
						console.log(this.banners)
						console.log(this.banners[0].image)
						console.log("tt")
					}
				})
			},
			/*getsum(input) {
				uni.request({
					url:`http://127.0.0.1:4444/orders/orders?id=${input}`,
					data: {
						//id:this.order_id
					},
					method:"GET",
					success: (res) => {
						this.sum=res.data.orders
						console.log(res.data); 
						
						console.log("tts")
						console.log(this.sum)

						console.log("tt")
					}
				})
			},*/
			
			
			gotoorder(item){
				uni.reLaunch({
					url:"../order/order"
				})
			},
			onLoad(options) {
				this.order_id = options.id;
				this.getdata();
				console.log("ttsss")
				console.log(this.order_id)
				//this.getsum(this.order_id-1)
			},
			
			
			gotodetail(id) {
				
				console.log(id)
				uni.navigateTo({
					url:`../gooddetail/gooddetail?id=${id}`//填货物id
				})
			},
			getStatus(statusNumber){
				if(statusNumber==0){return "Pending"}
				if(statusNumber==1){return "Hold"}
				if(statusNumber==2){return "Shipped"}
				if(statusNumber==3){return "Cancelled"}
				return "error"
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
	
	.orderInformation{
		font-size: 170%;
		background-color: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		padding-left: 80upx;
		border-bottom: 1upx solid #e7e7e7;
		padding-top: 20upx;
		padding-bottom: 20upx;
		color: #0081FF;
	}

</style>
