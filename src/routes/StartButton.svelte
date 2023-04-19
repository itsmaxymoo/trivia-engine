<script lang="ts">
	export let selectedTopics: Array<String> = [];
	export let isLoading: boolean = false;
</script>

<p class="has-text-centered">
	<button
		on:click
		class="button is-medium is-link {selectedTopics.length == 0
			? 'is-outlined is-static'
			: ''} {isLoading ? 'is-loading' : ''}"
	>
		{#if selectedTopics.length == 0}
			Select topic(s) to start
		{:else}
			Start!
		{/if}
	</button>
</p>
