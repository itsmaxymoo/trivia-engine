<script lang="ts">
	import type { Question } from "$lib/game";

	export let correct: boolean = true;
	export let question: Question = {
		text: "NULL",
		answer: "NULL",
		falseAnswers: [],
	};
</script>

<article class="message {correct ? 'is-success' : 'is-danger'}">
	<div class="message-header">
		<p>{correct ? "Correct!" : "Wrong!"}</p>
	</div>
	<div class="message-body">
		{#if correct}
			Congratulations! The correct answer is indeed {question.answer}.
		{:else}
			Try again next time! The correct answer is <b>{question.answer}</b>.
		{/if}
	</div>
</article>
