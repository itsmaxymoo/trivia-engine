<script lang="ts">
	import { createEventDispatcher } from "svelte";

	export let answers: Array<String> = [];
	export let multiSelect: boolean = false;
	let selectedAnswers: Array<String> = [];
	let isLoading: boolean = false;

	const eventDispatch = createEventDispatcher();

	function toggleAnswer(answer: String) {
		if (isLoading) {
			return;
		}
		// If we need to add this element
		if (!selectedAnswers.includes(answer)) {
			if (!multiSelect) {
				selectedAnswers = [];
			}

			selectedAnswers = [...selectedAnswers, answer];
		}
		// Else, we need to remove this element.
		else {
			selectedAnswers.splice(selectedAnswers.indexOf(answer), 1);
			selectedAnswers = selectedAnswers;
		}
	}

	function sendSelectedAnswers() {
		isLoading = true;
		eventDispatch("answersSelected", {
			answers: selectedAnswers,
		});
	}
</script>

<div class="box has-text-centered">
	<table class="table is-fullwidth is-hoverable is-striped">
		<tbody>
			{#each answers as answer}
				<tr
					on:click={() => {
						toggleAnswer(answer);
					}}
					class="hover-cursor {selectedAnswers.includes(answer)
						? 'is-selected'
						: ''}"
				>
					<td class="has-text-left">{answer}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<p class="has-text-centered">
	<button
		on:click={sendSelectedAnswers}
		class="button is-link {selectedAnswers.length == 0 || isLoading
			? 'is-outlined is-static'
			: ''} {isLoading ? 'is-loading' : ''}"
	>
		{#if selectedAnswers.length == 0}
			Select an answer...
		{:else}
			Check!
		{/if}
	</button>
</p>

<style>
	.hover-cursor {
		cursor: pointer;
	}
</style>
