<template>
	<view class="content">

		<!--Search bar-->
		<view class="nav" style="position: fixed;top: 0;width: 100%;z-index:9999">
			<view class="cu-bar search bg-gradual-blue">
				<view class="search-form round">
					<text @click="goods_search()" class="cuIcon-search"></text>
					<input v-model="keyword" placeholder="" />
				</view>
			</view>
		
			<!--Tab-->
			<view style="">
				<scroll-view class="nav bg-white" scroll-x>
					<view class=" justify-between">
						<view class="cu-item flex-sub" @click="sortbyprice">
							Sort
						</view>
						
					</view>
				</scroll-view>
			</view>
		</view>
		<view style="margin-top:190upx;">
			<view v-for="(p,i) in goods" :key="i">
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
				search: "",
				TabLists: ["Hot", "Fruit", "Vegetable", "Meat"],
				goods: [],
				keyword:""
			}
		},
		onLoad() {
			this.getgoods();
		},
		methods: {
			
			gotodetail(id) {
				
				console.log(id)
				uni.navigateTo({
					url:`../gooddetail/gooddetail?id=${id}`//填货物id
				})
			},
			
			sortbyprice(){
				this.goods.sort(function(a,b){
					return a.price - b.price
				})
			}
			,
			goods_search(){
				uni.request({
					url: "http://127.0.0.1:4444/goods/search",
					data: {
						keyword: this.keyword,
					},
					method: "POST",
					success: (res) => {
						if (res.data.status == 0) {
							var goodsInfo = res.data.result
							uni.setStorageSync("search_result",goodsInfo)
							console.log(goodsInfo)
							uni.navigateTo({
								url:"../searchgoods/searchgoods"
							})
						}
					}
				})
			},
			getgoods() {
				uni.request({
					url:"http://127.0.0.1:4444/goods/index",
					data:{
						
					},
					success:(res) =>{
						this.goods=res.data
						console.log(this.goods)
					}
					
					
				})
			},
		}
	}
</script>

<style>
</style>
