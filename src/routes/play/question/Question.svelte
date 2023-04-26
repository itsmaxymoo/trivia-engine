<script lang="ts">
	import { QuestionState, type Question } from "$lib/game";
	import Answers from "./Answers.svelte";
	import QuestionText from "./QuestionText.svelte";
	import Result from "./Result.svelte";

	export let question: Question = {
		text: "NULL",
		correctAnswers: [],
		falseAnswers: [],
	};
	export let questionAnswerState: QuestionState = QuestionState.UNANSWERED;
	let multiSelect: boolean = false;

	$: shuffledAnswers = [
		...question.falseAnswers,
		...question.correctAnswers,
	].sort(() => Math.random() - 0.5);

	$: {
		question;
		questionAnswerState = QuestionState.UNANSWERED;
		multiSelect = question.correctAnswers.length > 1;
	}
</script>

<QuestionText bind:text={question.text} />

{#if questionAnswerState == QuestionState.UNANSWERED}
	<Answers
		bind:answers={shuffledAnswers}
		on:answersSelected
		bind:multiSelect
	/>
{:else if questionAnswerState == QuestionState.TRUE}
	<Result {question} correct={true} />
{:else if questionAnswerState == QuestionState.FALSE}
	<Result {question} correct={false} />
{/if}
