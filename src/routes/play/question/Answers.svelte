<script lang="ts">
	export let answers: Array<String> = [];
	export let selectedAnswers: Array<String> = [];
	export let multiSelect: boolean = false;

	function toggleAnswer(answer: String) {
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

<style>
	.hover-cursor {
		cursor: pointer;
	}
</style>
