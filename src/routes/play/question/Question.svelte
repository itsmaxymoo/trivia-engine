<script lang="ts">
	import type { Question } from "$lib/game";
	import Answers from "./Answers.svelte";
	import QuestionText from "./QuestionText.svelte";

	export let question: Question = {
		text: "NULL",
		answer: "NULL",
		falseAnswers: [],
	};

	$: shuffledAnswers = [...question.falseAnswers, question.answer].sort(
		() => Math.random() - 0.5
	);
</script>

<QuestionText bind:text={question.text} />

<Answers bind:answers={shuffledAnswers} on:answersSelected />
