<template>
	<div class="filter-button">
		  <b-button variant="outline-success" :data-filter="theme.value" @click.prevent="filterByTheme">{{theme.value}}</b-button>
	</div>
</template>

<script>
	export default {
		props: ["theme", "filterByTheme"]
	}
</script>
<style>
.filter-button {
	margin: 5px;
}
</style>
