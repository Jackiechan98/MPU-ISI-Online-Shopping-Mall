<template>
	<view>
		
		<!--top-->
		<view class="flex bg-gradual-blue content1 justify-between align-center">
			<view class="flex justify-between">
				<view><image class="user-logo" src="../../static/client.jpg"></image></view>
				<view style="margin-left: 20upx;margin-top: 7upx;">
					<view class="user-name" v-if="!userIsLogin" @click="login">Login or register</view>
					<view class="user-name" v-if="userIsLogin">{{userInfo.uName}}</view>
					<view style="font-size: 130%;" v-if="userIsLogin"> ID:{{userInfo.uid}}</view>
					<view @tap="gotochange()" v-if="userIsLogin" style="font-size: 110%;color: #dddddd;">change password</view>
				</view>
			</view>
			<view>
				<button @tap="logout()" class="bg-grey list-item" v-if="userIsLogin" style="font-size: 110%;color:white;">Log out <text style="padding-left: 10upx; font-family: monospace; font-size: 130%;"> </text></button></view>
		</view>
		<!--top end-->
		
		<!--order status-->
		<view v-if="userIsLogin" @tap="gotoorder(userInfo.uid)" class="flex justify-center flex-direction bg-white statusTable">
			<view class="flex justify-between " style="width: 93%;margin-top: 15upx;" >
				<text> </text>
				<text style="color:#0081FF">All orders >></text>
			</view>
			<view class="bg-white flex justify-around" style="width: 730upx;height: 140upx;padding-top: 16upx;">
				<view style="position: relative;" class="flex align-center flex-direction" v-for="(p,i) in orders" :key="i">
					<view :class="p.icon" style="font-size: 60upx;color: grey;">						
					</view>
					<view v-if="status[i]!=0" style="position: absolute;top:1px;right: 2px;" class="cu-tag bg-gradual-blue round sm">
						{{status[i]}}
					</view>
					<view>
						{{p.text}}
					</view>
				</view>
			</view>
		</view>
		<!--end of order status-->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				status:[],
				user_id:"",
				userIsLogin:false,
				userInfo:"",
				orders:[
					{
						text:"Pending",
						icon:"cuIcon-pay",
					},
					{
						text:"Holding",
						icon:"cuIcon-pay",
					},
					{
						text:"Shipped",
						icon:"cuIcon-deliver",
					},
					{
						text:"Canceled",
						icon:"cuIcon-deliver",
					},
					
				]
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
			gopage(item){
				console.log(item);
				uni.reLaunch({
					url:"../login/login"
				})
			},
			gotochange(){
				uni.navigateTo({
					url:"../login/changepassword"
				})
			},
			login(){
				uni.reLaunch({
					url:"../login/login"
				})
			},
			logout(){
				var globalUser = this.getGlobalUser("globalUser")
				uni.removeStorageSync("globalUser")
				uni.navigateTo({
					
					url:"../login/login"
				})
			},
			gotoorder(input) {
				console.log(input)
				uni.navigateTo({
					url: `../order/order?id=${input}`
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
				 
			 	this.getstatus(userInfo.uid);
				console.log(userInfo.uid)
			},
			getstatus(input) {
				
				console.log(input)
				uni.request({
					url:`http://127.0.0.1:4444/users/my?id=${input}`,
					//data: {
					//	id:this.user_id
					//},
					method:"GET",
					success: (res) => {
						console.log(res.data)
						//console.log(res.data.status0[0].status0)
						
						this.status[0]=res.data.status0[0].status0
						this.status[1]=res.data.status1[0].status1
						this.status[2]=res.data.status2[0].status2
						this.status[3]=res.data.status3[0].status3
						this.$forceUpdate()
						console.log("tt")
					}
				})
			},
		}
	}
</script>

<style>
.user-logo{
	width: 130upx;
	height: 130upx;
}

.content1{
	padding: 30upx 30upx 30upx 30upx;
}
.user-name{
	font-size: 130%;
}

.total{
	position: fixed;
	bottom: 90upx;
	width: 750upx;
	height: 90upx;
	background-color: white;
	padding-left: 30upx;
	padding-right: 35upx;
}
.statusTable{
	border-top: 1upx solid #e7e7e7;
}
</style>
