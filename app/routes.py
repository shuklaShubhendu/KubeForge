from flask import Blueprint, request, render_template, redirect, url_for, current_app
from bson.objectid import ObjectId
from datetime import datetime

habit_bp = Blueprint('habit', __name__)

@habit_bp.route('/')
def index():
    habits = list(current_app.db.habits.find())
    return render_template('index.html', habits=habits)

@habit_bp.route('/add', methods=['POST'])
def add_habit():
    habit_name = request.form.get('habit')
    if habit_name:
        current_app.db.habits.insert_one({
            'habit': habit_name,
            'created_at': datetime.utcnow(),
            'logs': [],       # daily log timestamps
            'streak': 0
        })
    return redirect(url_for('habit.index'))

@habit_bp.route('/log/<habit_id>', methods=['POST'])
def log_progress(habit_id):
    habit = current_app.db.habits.find_one({'_id': ObjectId(habit_id)})
    today = datetime.utcnow().date()

    # Check if already logged today
    log_dates = [log.date() for log in map(lambda ts: ts.date(), [log for log in habit['logs']])]
    if today not in log_dates:
        habit['logs'].append(datetime.utcnow())
        streak = habit.get('streak', 0) + 1
        current_app.db.habits.update_one(
            {'_id': ObjectId(habit_id)},
            {'$set': {'logs': habit['logs'], 'streak': streak}}
        )
    return redirect(url_for('habit.index'))

@habit_bp.route('/delete/<habit_id>')
def delete_habit(habit_id):
    current_app.db.habits.delete_one({'_id': ObjectId(habit_id)})
    return redirect(url_for('habit.index'))
