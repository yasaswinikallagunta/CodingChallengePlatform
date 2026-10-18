import { htmlTopic } from './topics/htmlTopic';
import { cssBasicsTopic } from './topics/cssBasicsTopic';
import { advancedCssTopic } from './topics/advancedCssTopic';
import { jsBasicsTopic } from './topics/jsBasicsTopic';
import { advancedJsTopic } from './topics/advancedJsTopic';
import { reactTopic } from './topics/reactTopic';
import { mongoTopic } from './topics/mongoTopic';
import { deploymentTopic } from './topics/deploymentTopic';

export const COURSE_METADATA = {
  id: 'modern-frontend-development',
  slug: 'modern-frontend-development',
  title: 'Modern Frontend Development',
  badge: 'Complete Career Curriculum',
  level: 'Beginner to Advanced',
  description: 'Master industry-grade frontend and modern web engineering. From semantic HTML5 structures and responsive CSS layouts to advanced JavaScript patterns, interactive React architectures, MongoDB data persistence, and production deployment pipelines.',
  totalTopics: 8,
  totalExercises: 40,
  estimatedHours: 60,
  skillsCovered: [
    'HTML5 Semantic Architecture & Accessibility (ARIA)',
    'Responsive CSS3, Flexbox, Grid & Modern Themes',
    'Modern ES6+ JavaScript, Closures & Asynchronous Patterns',
    'React Component Lifecycle, Hooks, State & Context',
    'MongoDB Document Models, CRUD & Aggregations',
    'Cloud Production Deployments, CI/CD & Performance'
  ]
};

export const COURSE_TOPICS = [
  htmlTopic,
  cssBasicsTopic,
  advancedCssTopic,
  jsBasicsTopic,
  advancedJsTopic,
  reactTopic,
  mongoTopic,
  deploymentTopic
];

export const getTopicBySlug = (slug) => {
  return COURSE_TOPICS.find((t) => t.id === slug) || COURSE_TOPICS[0];
};

export const getAllExercises = () => {
  return COURSE_TOPICS.flatMap((topic) =>
    (topic.exercises || []).map((exercise) => ({
      ...exercise,
      topicId: topic.id,
      topicTitle: topic.title
    }))
  );
};
