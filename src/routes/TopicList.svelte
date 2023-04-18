<script lang="ts">
	let loaded: Boolean = false;
</script>

<div class="box">
	<h2 class="is-size-3 is-underlined">Topics</h2>

	{#if loaded}
		loaded
	{:else}
		<button class="button is-fullwidth is-loading is-link is-medium"></button>
	{/if}
</div>
