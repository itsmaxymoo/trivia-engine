<script lang="ts">
	import { appName } from "$lib/const";
</script>

<svelte:head>
	<title>{appName}</title>
</svelte:head>

<div class="content">
	<slot />
</div>
