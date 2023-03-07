<template>
	<view class="bg-white">
		<view class="cu-bar bg-gradual-blue">
			<view @tap="navigateBack()" class="action">
				<text class="cuIcon-back text-white"> Back</text>
			</view>
		</view>
		
		<view>
			<swiper class="swiperStyle">
				<swiper-item v-for="(p,i) in banners" :key="i">
						<image mode="widthFix" class="bannerimg align-center" :src="p.image"></image>
				</swiper-item>
				<swiper-item v-if="p.image2" v-for="(p,i) in banners" :key="i">
					<image mode="widthFix" class="bannerimg align-center" :src="p.image2"></image>
				</swiper-item>
				<swiper-item v-if="p.image3" v-for="(p,i) in banners" :key="i">
					<image mode="widthFix" class="bannerimg align-center" :src="p.image3"></image>
				</swiper-item>
				<swiper-item v-if="p.image4" v-for="(p,i) in banners" :key="i">
					<image mode="widthFix" class="bannerimg align-center" :src="p.image4"></image>
				</swiper-item>
				<swiper-item v-if="p.image5" v-for="(p,i) in banners" :key="i">
					<image mode="widthFix" class="bannerimg align-center" :src="p.image5"></image>
				</swiper-item>
			</swiper>
			
		</view>
		 
		<view class="cu-bar bg-white">
			<div class="text-bold">
				<text style="font-size: 22px;color: #09a3ea;"> Price:${{detail.price}}</text>
			</div>
			<div><text style="font-size: 12px;color: #09a3ea;margin: 1px;">Inventory:{{detail.remaining}}</text></div>	
		</view>
	
		<view class="cu-bar bg-white">
			<div><text style="font-size: 18px;font-weight: bold;color: #000000;margin: 1px;">{{detail.goods_name}}</text></div>
		</view>

		<view class="cu-bar bg-white">
			<div><text style="font-size: 20px;font-weight: bold;color: #000000;">Product describtion:</text></div>
		</view>
		</Br>

		<view class="contentShow" style="margin-left: 10px;margin-right: 10px;">
			<view style="padding: 12upx;">
			{{detail.description}}
			</view>
		</view>


		<view class="cu-bar barfixed bg-white tabbar border shop justify-between">
			<view>
				<button @tap="gotocart()" class="action">
					<view class="cuIcon-cart"></view>
						back to cart
				</button>
			</view>
			<view class="addToCart" v-if="userIsLogin">
				<button @click="addCart(detail.goods_id,userInfo.uid)" class="bg-gradual-blue round submit" style="width: 400upx;">
					<text style="font-size: 20px;">
						Add to cart
					</text>
					
				</button>
			</view>
			<view class="addToCart" v-if="!userIsLogin">
				<button @tap="gotologin()" class="bg-gradual-blue round submit" style="width: 400upx;">
					<text style="font-size: 20px;">
						Add to cart
					</text>
					
				</button>
			</view>
		</view>


	</view>
</template>

<script>
	export default {
		data() {
			
			return {
				goods_id:"",
				detail: {
					
				},
				userIsLogin:false,
				banners: [],
				userInfo:"",
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
					url:"http://127.0.0.1:4444/goods/details",
					data: {
						id:this.goods_id
					},
					method:"GET",
					success: (res) => {
						this.banners = res.data.banners;
						this.detail = res.data.detail;
						//console.log(res.data.detail); 
						//console.log(this.banners);
						//console.log(this.detail);
						console.log(res.data);
					}
				})
			},
			navigateBack() {
				uni.navigateBack({
				})
			},
			
			backtogoods() {
				uni.switchTab({
					url: "../goods/goods"
				})
			},
			gotocart() {
				uni.switchTab({
					url: "../carts/carts"
				})
			},
			addCart(goodsid,userid) {
				uni.request({
					url:"http://127.0.0.1:4444/goods/addcart?id="+goodsid+"&uid="+userid
				
				})
				uni.showToast({
					icon: "none",
					title: "Added successfully"
				})
				
				uni.switchTab({
					url:"../carts/carts",
					
				})
				location.reload()
				
			},
			gotologin(){
				uni.navigateTo({
					url:"../login/login"
				})
			}
			,
		},
		onLoad(options) {
			this.goods_id = options.id;
			this.getdata();
			
		},

	}
</script>

<style>
	.addToCart {
		
	}
	div {
		margin: 10px;
	}

	.barfixed {
		position: fixed;
		width: 750upx;
		bottom: 0upx;
		height: 10upx;
	}

	.zhanwei {
		width: 620upx;
		height: var(--status-bar-height);
	}

	.bannerimg {
		width: 620upx;
		height: 5px;
	}
	
	.contentShow{
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		background-color: #d9e7df;
		color: black;
		border-radius: 8upx;
	}
	
	.swiperStyle{
		width: 100%;
		height: 500upx;
		aligin: center;
	}
</style>
