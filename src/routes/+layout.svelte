<script>
	import { appName } from "$lib/const";
</script>

<svelte:head>
	<title>{ appName }</title>
</svelte:head>

<section class="section pt-5">
	<div class="container">
		<div class="content">
			<slot />
		</div>
	</div>
</section>
