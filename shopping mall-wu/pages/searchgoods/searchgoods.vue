<template>
	<view class="content">

		
		<view style="margin-top:0upx;">
			<view v-for="(p,i) in goodsInfo" :key="i">
				<view @tap="gotodetail(p.goods_id)" style="padding:20upx 20upx 20upx 1upx;border-bottom: 1upx solid #e7e7e7;" class="flex justify-around bg-white">
					<view style="width: 300upx;">
						<image style="width: 180upx;height: 200upx;margin-left: 70upx;" :src="p.image"></image>
					</view>
					<view style="width: 440upx; margin-top: 35upx;borflex-direction: column; ">
						<view style=" font-size: 110%;">
							{{p.goods_name}}
						</view>
						<view style="font-size: 130%;padding-top: 10upx;">
							<text style="color: #06618c;"><text style="font-size: 85%;">$</text>{{p.price}}</text>
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
				goods: [],
			}
		},
		onShow(){
			var goodsInfo = this.getsearch_result("search_result")
			if(goodsInfo!=null){
				this.goodsInfo = goodsInfo;
			}else{
				this.goodsInfo = {};
			}
			
		},
		
		methods: {
			
			gotodetail(id) {
				
				console.log(id)
				uni.navigateTo({
					url:`../gooddetail/gooddetail?id=${id}`//填货物id
				})
			}
			,
			
		}
	}
</script>

<style>
</style>


