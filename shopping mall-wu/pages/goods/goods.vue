<template>
	<view>
		<!--Search bar-->
		<view class="cu-bar search bg-gradual-blue">
			<view class="search-form round">
				<text @click="goods_search()" class="cuIcon-search"></text>
				<input v-model="keyword" placeholder="" class="log-input"/>
			</view>
		</view>

		<!--main part-->
		<view class="flex">
			<!--left part-->
			<scroll-view scroll-y style="height: calc(100vh - 194upx); width: 180upx;">
				<view @tap="select(i)" :style="{color:selected==i?'#06618c':'#767676',fontSize:selected==i?'100%':'100%'}" :class="selected==i?'bg-white':''"
				 class="type-item" v-for="(p,i) in goods" :key="i">
					{{p.brand_name}}
				</view>
			</scroll-view>
			<!--right part-->
			<scroll-view scroll-with-animation :scroll-into-view="'good-'+selected" class="bg-white" scroll-y style="height: calc(100vh - 194upx); width: 570upx;">
				<view :id="'good-'+i" style="border-bottom: 0.5upx #E7E7E7 solid;padding-bottom: 40upx;" v-for="(p,i) in goods" :key="i">
					<view class="g-title">{{p.brand_name}}</view>
					<view class="flex flex-wrap">
						<view @tap="gotodetail(tp.goods_id)" class="flex justify-center align-center" style="width: 275upx;margin-top: 10upx;" v-for="(tp,ti) in p.data" :key="ti">
							<view>
								<image style="width: 170upx;height: 220upx;" :src="tp.image"></image>
								<view style="text-align: center;">{{tp.goods_name}}</view>							
							</view>
						</view>
					</view>
				</view>
			</scroll-view>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				search: "",
				types: [],
				goods: [],
				selected: 0,
				keyword:"",
			}
		},
		methods: {
			
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
			
			gotodetail(id) {
				
				console.log(id)
				uni.navigateTo({
					url:`../gooddetail/gooddetail?id=${id}`//填货物id
				})
			},

			getgoods() {
				uni.request({
					url:"http://127.0.0.1:4444/goods/brand_lists",
					data:{
						
					},
					success:(res) =>{
						this.goods=res.data
						console.log(res.data)
					}
					
					
				})
			},

			select(i) {
				this.selected = i
			}
		},

		onLoad() {
			this.getgoods()
		},
		
	}
</script>

<style>
	.type-item {
		height: 100upx;
		text-align: center;
		line-height: 100upx;
	}
	
	.g-title{
		font-size: 120%;
		margin-top: 30upx;
		margin-bottom: 20upx;
		margin-left: 30upx;
	}
</style>
