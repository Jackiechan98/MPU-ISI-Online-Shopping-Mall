<template>
	<view class="loginpage bg-white">
	
	
		<!--title-->
		<view style="padding-top: 40upx;">
			<view @tap="gotohome()" style="padding-bottom: 60upx;margin-left: 32upx;">
				<image src="../../static/icon/back.png" style="width: 70upx;height: 70upx;"></image>
			</view>
			<view class="title">
				<view style="font-size: 170%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">Processed
					with your</view>
				<text class="login">Register</text>
			</view>
		</view>
	
		<!--input box-->
		<view class="input-fa">
			<view style="margin-top: 30upx;">
				Userid (use userid to log in)
			</view>
			<view>
				<input class="log-input" v-model="form.Userid"/>
			</view>
			<view style="margin-top: 30upx;">
				Username
			</view>
			<view>
				<input class="log-input" v-model="form.username"/>
			</view>
			<view style="margin-top: 30upx;">
				Password
			</view>
			<view>
				<input class="log-input" v-model="form.Password" :password="true"/>
			</view>
			<view style="margin-top: 30upx;">
				Email
			</view>
			<view>
				<input class="log-input" v-model="form.email"/>
			</view>
			<view style="margin-top: 30upx;">
				Shipping address
			</view>
			<view>
				<input class="log-input" v-model="form.uAddress"/>
			</view>
		</view>
	
		<!--Register button-->
		<view style="margin-top: 50upx;" class="flex justify-center">
			<button @tap="Register()" class="bg-gradual-blue" style="width: 450upx;">
				Register
			</button>
		</view>
	
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					Userid: "",
					password: "",
					uAddress:"",
					email:"",
					username:""
				}
			}
		},
		methods: {
			gotohome(){
				uni.navigateTo({
					url:"../login/login"
				})
			},
			Register(){
				uni.request({
					url: "http://127.0.0.1:4444/user/register",
					data: {
						userid: this.form.Userid,
						password: this.form.Password,
						uAddress: this.form.uAddress,
						username: this.form.username,
						email: this.form.email
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: res.data.desc
						})
						console.log(res.data)
						if (res.data.status == 0) {
							var userInfo = res.data
							console.log(userInfo.uName)
							uni.setStorageSync("uid",res.data.userid)
							uni.setStorageSync("globalUser",userInfo)
							uni.switchTab({
								url: "../my/my"
							})
						}
					}
				})
			}
		}
	}
</script>

<style>
.loginpage {
		height: 1200upx;
	}
page {
	background-color: white;
	}
	.title {
		margin-left: 50upx;
	}

	.login {
		font-size: 250%;
		font-weight: bold;
		color: black;
	}

	.log-input {
		height: 70upx;
		border-bottom: 1upx solid #e7e7e7;
	}

	.input-fa {
		padding-left: 55upx;
		padding-right: 80upx;
		margin-top: 70upx;
	}
</style>
