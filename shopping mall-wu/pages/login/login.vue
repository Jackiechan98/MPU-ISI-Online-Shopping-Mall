<template>
	
	<view class="loginpage bg-white">
		
		
		<!--title-->
		<view  style="padding-top: 40upx;">
			<view @tap="gotomy()" style="padding-bottom: 60upx;margin-left: 32upx;"><image src="../../static/icon/back.png" style="width: 70upx;height: 70upx;"></image></view>
			<view class="title">
				<view style="font-size: 170%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Processed with your</view>
				<text class="login">Login</text>
			</view>
		</view>
		
		<!--input box-->
		<view class="input-fa">
			<view>
				Userid
			</view>
			<view>
				<input class="log-input"  v-model="form.Userid"/>
			</view>
			<view style="margin-top: 30upx;">
				Password
			</view>
			<view>
				<input class="log-input" v-model="form.password" :password="true"/>
			</view>
		</view>
		
		<!--login button-->
		<view style="margin-top: 80upx;" class="flex justify-center">
			<button @tap="login" class="bg-gradual-blue" style="width: 450upx;">
				Login
			</button>
		</view>
		
		<!--change passwoed-->
		<!-- <view class="flex justify-center" style="margin-top: 15upx;">
			<text style="color:#b1b4b5;font-size: 90%;">Forget your password?</text>
		</view> -->
		
		<view class="flex justify-center" style="margin-top: 280upx;">
			<text @tap="register()" style="color:#06618c;font-size: 90%;">Not a member? Sign Up</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form:{
					Userid:"",
					password:""
				},
			userIsLogin:false
			}
		},
		methods: {
			login(){
				uni.request({
					url:"http://127.0.0.1:4444/user/login",
				data:{
					userid:this.form.Userid,
					password:this.form.password
				},
				method:"POST",
				success:(res) =>  {
					uni.showToast({
						icon:"none",
						title:res.data.desc
					})
					if(res.data.status==0){
						var userInfo = res.data.info
						console.log(userInfo)
						uni.setStorageSync("uid",res.data.userid)
						uni.setStorageSync("globalUser",userInfo)
						history.back()
					}
					// else
					// uni.navigateTo({
					// url:"http://127.0.0.1:4444/my/my",
					// })
				}
				})
			},
			gotohome(){
				uni.switchTab({
					url:"../index/index"
				})
			},
			gotomy(){
				uni.switchTab({
					url:"../my/my"
				})
			},
			register(){
				uni.navigateTo({
					url:"../login/register"
				})
			}
			
		}
	}
</script>

<style>
.loginpage{
	height: 100%;
}	

.title{
	margin-left: 50upx;
}

.login{
	font-size: 250%;
	font-weight: bold;
	color:black;
}
.log-input{
	height: 70upx;
	border-bottom:1upx solid #e7e7e7;
}
.input-fa{
	padding-left: 55upx ;
	padding-right: 80upx;
	margin-top: 150upx;
}
page {
	background-color: white;
	}
</style>
