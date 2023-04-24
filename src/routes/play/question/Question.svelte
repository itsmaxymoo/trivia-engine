<script lang="ts">
	import { QuestionState, type Question } from "$lib/game";
	import Answers from "./Answers.svelte";
	import QuestionText from "./QuestionText.svelte";
	import Result from "./Result.svelte";

	export let question: Question = {
		text: "NULL",
		answer: "NULL",
		falseAnswers: [],
	};
	export let questionAnswerState: QuestionState = QuestionState.UNANSWERED;

	$: shuffledAnswers = [...question.falseAnswers, question.answer].sort(
		() => Math.random() - 0.5
	);

	$: {
		question;
		questionAnswerState = QuestionState.UNANSWERED;
	}
</script>

<QuestionText bind:text={question.text} />

{#if questionAnswerState == QuestionState.UNANSWERED}
	<Answers bind:answers={shuffledAnswers} on:answersSelected />
{:else if questionAnswerState == QuestionState.TRUE}
	<Result {question} correct={true} />
{:else if questionAnswerState == QuestionState.FALSE}
	<Result {question} correct={false} />
{/if}
