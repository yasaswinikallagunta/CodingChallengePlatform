import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import HtmlCssSandbox from './HtmlCssSandbox';
import JsSandbox from './JsSandbox';
import ReactSandbox from './ReactSandbox';
import MongoSandbox from './MongoSandbox';
import DeploymentSandbox from './DeploymentSandbox';
import { 
  CheckCircle2, 
  HelpCircle, 
  Eye, 
  EyeOff, 
  Copy, 
  Check, 
  ArrowRight, 
  RotateCcw, 
  Lightbulb, 
  Award,
  ChevronRight,
  Info
} from 'lucide-react';

export default function ExerciseWorkspace({
  topic,
  completedMap = {},
  userCodesMap = {},
  onSaveProgress,
  onNextTopic
}) {
  const [selectedExerciseIndex, setSelectedExerciseIndex] = useState(0);
  const [userCode, setUserCode] = useState('');
  const [showHints, setShowHints] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [copiedSolution, setCopiedSolution] = useState(false);

  const exercises = topic.exercises || [];
  const currentExercise = exercises[selectedExerciseIndex] || exercises[0];

  // Sync userCode when exercise changes
  useEffect(() => {
    if (!currentExercise) return;
    const key = `${topic.id}-${currentExercise.id}`;
    const savedCode = userCodesMap[key];
    setUserCode(savedCode !== undefined ? savedCode : currentExercise.starterCode || '');
    setShowHints(false);
    setShowSolution(false);
  }, [currentExercise?.id, topic.id]);

  if (!currentExercise) {
    return <div className="p-8 text-center text-slate-500">No exercises found for this topic.</div>;
  }

  const isCurrentCompleted = !!completedMap[`${topic.id}-${currentExercise.id}`];

  const handleCodeChange = (newCode) => {
    setUserCode(newCode);
  };

  const handleResetCode = () => {
    setUserCode(currentExercise.starterCode || '');
  };

  const handleMarkCompleted = async () => {
    try {
      confetti({
        particleCount: 80,
        spread: 60,
        origin: { y: 0.7 }
      });
      await onSaveProgress(topic.id, currentExercise.id, true, userCode);
    } catch (err) {
      console.error('Error saving progress:', err);
    }
  };

  const handleToggleCompleted = async () => {
    const nextState = !isCurrentCompleted;
    if (nextState) {
      confetti({
        particleCount: 80,
        spread: 60,
        origin: { y: 0.7 }
      });
    }
    await onSaveProgress(topic.id, currentExercise.id, nextState, userCode);
  };

  const handleCopySolution = () => {
    navigator.clipboard.writeText(currentExercise.solution || '');
    setCopiedSolution(true);
    setTimeout(() => setCopiedSolution(false), 2000);
  };

  const handleNextExercise = () => {
    if (selectedExerciseIndex < exercises.length - 1) {
      setSelectedExerciseIndex(selectedExerciseIndex + 1);
    } else if (onNextTopic) {
      onNextTopic();
    }
  };

  const getDifficultyBadge = (diff) => {
    switch (diff?.toLowerCase()) {
      case 'easy':
        return 'bg-emerald-100 text-emerald-800 border-emerald-200';
      case 'medium':
        return 'bg-amber-100 text-amber-800 border-amber-200';
      case 'hard':
        return 'bg-rose-100 text-rose-800 border-rose-200';
      default:
        return 'bg-slate-100 text-slate-800 border-slate-200';
    }
  };

  const renderActiveSandbox = () => {
    const type = currentExercise.type?.toLowerCase();

    if (type === 'html' || type === 'css') {
      return (
        <HtmlCssSandbox
          exercise={currentExercise}
          userCode={userCode}
          onChange={handleCodeChange}
          onReset={handleResetCode}
          onComplete={handleMarkCompleted}
          isCompleted={isCurrentCompleted}
        />
      );
    }

    if (type === 'react') {
      return (
        <ReactSandbox
          exercise={currentExercise}
          userCode={userCode}
          onChange={handleCodeChange}
          onReset={handleResetCode}
          onComplete={handleMarkCompleted}
          isCompleted={isCurrentCompleted}
        />
      );
    }

    if (type === 'mongo' || type === 'mongodb') {
      return (
        <MongoSandbox
          exercise={currentExercise}
          userCode={userCode}
          onChange={handleCodeChange}
          onReset={handleResetCode}
          onComplete={handleMarkCompleted}
          isCompleted={isCurrentCompleted}
        />
      );
    }

    if (type === 'deployment' || type === 'devops') {
      return (
        <DeploymentSandbox
          exercise={currentExercise}
          userCode={userCode}
          onChange={handleCodeChange}
          onReset={handleResetCode}
          onComplete={handleMarkCompleted}
          isCompleted={isCurrentCompleted}
        />
      );
    }

    // Default to JavaScript sandbox
    return (
      <JsSandbox
        exercise={currentExercise}
        userCode={userCode}
        onChange={handleCodeChange}
        onReset={handleResetCode}
        onComplete={handleMarkCompleted}
        isCompleted={isCurrentCompleted}
      />
    );
  };

  return (
    <div className="space-y-6">
      {/* Exercise Navigation Tabs (Exactly 5 distinct practice exercises) */}
      <div className="bg-white p-3 rounded-2xl border border-slate-200 shadow-xs">
        <div className="flex items-center justify-between mb-2 px-2">
          <span className="text-xs font-bold text-slate-600 uppercase tracking-wider">
            Practice Exercises (5 Required)
          </span>
          <span className="text-xs font-semibold text-emerald-700">
            {exercises.filter(ex => completedMap[`${topic.id}-${ex.id}`]).length} of {exercises.length} Completed
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-5 gap-2">
          {exercises.map((ex, idx) => {
            const isSelected = idx === selectedExerciseIndex;
            const isDone = !!completedMap[`${topic.id}-${ex.id}`];

            return (
              <button
                key={ex.id}
                onClick={() => setSelectedExerciseIndex(idx)}
                className={`p-2.5 rounded-xl text-left border transition relative flex flex-col justify-between ${
                  isSelected
                    ? 'border-emerald-600 bg-emerald-50/70 shadow-xs'
                    : 'border-slate-200 bg-white hover:border-slate-300'
                }`}
              >
                <div className="flex items-center justify-between gap-1 mb-1">
                  <span className="text-xs font-bold text-slate-900">Task {idx + 1}</span>
                  {isDone && <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />}
                </div>
                <div className="flex items-center justify-between">
                  <span
                    className={`text-[10px] font-bold px-1.5 py-0.5 rounded border ${getDifficultyBadge(
                      ex.difficulty
                    )}`}
                  >
                    {ex.difficulty}
                  </span>
                  <span className="text-[10px] text-slate-400 capitalize">{ex.type}</span>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Problem Statement & Requirements Card */}
      <div className="p-6 bg-white rounded-2xl border border-slate-200 shadow-xs space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span
              className={`text-xs font-bold px-2.5 py-1 rounded-full border ${getDifficultyBadge(
                currentExercise.difficulty
              )}`}
            >
              {currentExercise.difficulty}
            </span>
            <h2 className="text-lg font-black text-slate-900">{currentExercise.title}</h2>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={handleToggleCompleted}
              className={`px-4 py-2 rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5 ${
                isCurrentCompleted
                  ? 'bg-emerald-100 text-emerald-800 border border-emerald-300 hover:bg-emerald-200'
                  : 'bg-emerald-600 hover:bg-emerald-700 text-white'
              }`}
            >
              <CheckCircle2 className="w-4 h-4" />
              <span>{isCurrentCompleted ? 'Completed ✓' : 'Mark as Completed'}</span>
            </button>
          </div>
        </div>

        <p className="text-sm text-slate-700 leading-relaxed font-medium">
          {currentExercise.problemStatement}
        </p>

        {/* Requirements Checklist */}
        {currentExercise.requirements && currentExercise.requirements.length > 0 && (
          <div className="p-4 bg-slate-50 rounded-xl border border-slate-200">
            <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">
              Implementation Requirements
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-700">
              {currentExercise.requirements.map((req, rIdx) => (
                <li key={rIdx} className="flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 mt-1.5 shrink-0" />
                  <span>{req}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {currentExercise.expectedBehavior && (
          <div className="text-xs text-slate-600 flex items-start gap-2">
            <Info className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
            <span>
              <strong className="text-slate-800">Expected Outcome:</strong> {currentExercise.expectedBehavior}
            </span>
          </div>
        )}
      </div>

      {/* Main Interactive Sandbox */}
      <div className="w-full">
        {renderActiveSandbox()}
      </div>

      {/* Hints, Solution & Next Navigation Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Hints Card */}
        <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <Lightbulb className="w-4 h-4 text-amber-500" />
                Practice Hints ({currentExercise.hints?.length || 0})
              </span>
              <button
                onClick={() => setShowHints(!showHints)}
                className="text-xs font-bold text-emerald-700 hover:text-emerald-800 transition"
              >
                {showHints ? 'Hide Hints' : 'Reveal Hints'}
              </button>
            </div>

            {showHints ? (
              <ul className="space-y-2 text-xs text-slate-700">
                {(currentExercise.hints || []).map((hint, hIdx) => (
                  <li key={hIdx} className="p-2.5 rounded-lg bg-amber-50/70 border border-amber-200/60 leading-relaxed">
                    <strong className="text-amber-800">Hint {hIdx + 1}:</strong> {hint}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-xs text-slate-500 italic">
                Stuck on this challenge? Click Reveal Hints for step-by-step guidance without spoiling the code.
              </p>
            )}
          </div>
        </div>

        {/* Solution Card */}
        <div className="p-5 bg-white rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <Award className="w-4 h-4 text-emerald-600" />
                Verified Reference Solution
              </span>
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="text-xs font-bold text-emerald-700 hover:text-emerald-800 transition flex items-center gap-1"
              >
                {showSolution ? (
                  <>
                    <EyeOff className="w-3.5 h-3.5" />
                    <span>Hide Solution</span>
                  </>
                ) : (
                  <>
                    <Eye className="w-3.5 h-3.5" />
                    <span>Show Solution</span>
                  </>
                )}
              </button>
            </div>

            {showSolution ? (
              <div className="space-y-3">
                <div className="relative">
                  <div className="absolute top-2 right-2 z-10">
                    <button
                      onClick={handleCopySolution}
                      className="px-2.5 py-1 bg-slate-800/90 hover:bg-slate-700 text-white text-[11px] font-bold rounded flex items-center gap-1 transition"
                    >
                      {copiedSolution ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                      <span>{copiedSolution ? 'Copied' : 'Copy'}</span>
                    </button>
                  </div>
                  <pre className="p-3 bg-slate-900 text-emerald-300 rounded-xl text-xs font-mono overflow-x-auto max-h-56 leading-relaxed">
                    <code>{currentExercise.solution}</code>
                  </pre>
                </div>

                {currentExercise.solutionExplanation && (
                  <div className="p-2.5 rounded-lg bg-emerald-50 border border-emerald-200 text-xs text-slate-700 leading-relaxed">
                    <strong className="text-emerald-800 block mb-1">Solution Breakdown:</strong>
                    {currentExercise.solutionExplanation}
                  </div>
                )}
              </div>
            ) : (
              <p className="text-xs text-slate-500 italic">
                Attempt the challenge first! When you are ready to review clean engineering solutions, reveal the code here.
              </p>
            )}
          </div>
        </div>
      </div>

      {/* Advance to Next Exercise / Topic Bar */}
      <div className="p-4 bg-emerald-50/80 rounded-2xl border border-emerald-200 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <CheckCircle2 className="w-5 h-5 text-emerald-600" />
          <span className="text-xs sm:text-sm font-bold text-emerald-950">
            {isCurrentCompleted
              ? 'Great job completing this task! Ready to conquer the next?'
              : 'Save your progress by clicking Mark as Completed once your code works.'}
          </span>
        </div>

        <button
          onClick={handleNextExercise}
          className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-xs transition flex items-center gap-1.5 ml-auto"
        >
          <span>
            {selectedExerciseIndex < exercises.length - 1
              ? `Next Exercise (${selectedExerciseIndex + 2} of 5)`
              : 'Next Syllabus Topic'}
          </span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
