<script lang="ts">
	export let selectedTopics: Array<String> = [];
</script>

<p class="has-text-centered">
	<button
		class="button is-medium is-link {selectedTopics.length == 0
			? 'is-outlined is-static'
			: ''}"
	>
		{#if selectedTopics.length == 0}
			Select topic(s) to start
		{:else}
			Start!
		{/if}
	</button>
</p>
