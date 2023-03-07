<template>
	<view class="loginpage bg-white">
	
	
		<!--title-->
		<view style="padding-top: 40upx;">
			<view @tap="gotohome()" style="padding-bottom: 60upx;margin-left: 32upx;">
				<image src="../../static/icon/back.png" style="width: 70upx;height: 70upx;"></image>
			</view>
			<view class="title">
				<view style="font-size: 170%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
					Change your
				</view>
				<text class="login">Password</text>
			</view>
		</view>
	
		<!--input box-->
		<view class="input-fa">
			<view style="margin-top: 30upx;">
				Userid
			</view>
			<view>
				<input class="log-input" v-model="form.Userid"/>
			</view>
			<view style="margin-top: 30upx;">
				Your Old Password
			</view>
			<view>
				<input class="log-input" v-model="form.oldpassword" :password="true"/>
			</view>
			<view style="margin-top: 30upx;">
				Your New Password
			</view>
			<view>
				<input class="log-input" v-model="form.newpassword" :password="true"/>
			</view>
		</view>
	
		<!--Register button-->
		<view style="margin-top: 50upx;" class="flex justify-center">
			<button @tap="changepassword()" class="bg-gradual-blue" style="width: 450upx;">
				Confirm
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
					oldpassword: "",
					newpassword:""
				}
			}
		},
		methods: {
			gotohome(){
				uni.switchTab({
					url:"../my/my"
				})
			},
			changepassword(){
				uni.request({
					url: "http://127.0.0.1:4444/user/changepw",
					data: {
						userid: this.form.Userid,
						oldpassword: this.form.oldpassword,
						newpassword: this.form.newpassword,
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: res.data.desc
						})
						if (res.data.status == 0) {
							var userInfo = res.data
							console.log(userInfo)
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
