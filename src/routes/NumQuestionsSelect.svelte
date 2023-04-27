<script lang="ts">
	export let maxQuestions: number;
	export let selectedValue: number = 0;

	$: {
		maxQuestions;
		selectedValue = maxQuestions;
	}
</script>

<p class="has-text-centered">
	{#if maxQuestions !== undefined}
		<span class="select is-medium">
			<select bind:value={selectedValue}>
				<option value={maxQuestions}
					>All Questions ({maxQuestions})</option
				>
			</select>
		</span>
	{:else}
		<button class="button is-medium is-static is-loading">Loading</button>
	{/if}
</p>
