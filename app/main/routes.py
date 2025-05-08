from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from app import db
from app.main import bp
from app.main.forms import ReportForm
from app.models import Report

@bp.route('/')
@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', title='Dashboard')

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = ReportForm()
    if form.validate_on_submit():
        # Create report record
        report = Report(
            title=form.title.data,
            job_content=form.job_content.data,
            description=form.describe.data,
            result_content=form.result.data,
            author=current_user
        )
        if form.file.data is not None:
            file = form.file.data
            filename = secure_filename(file.filename)
            # Check if the file is allowed
            if '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']:
                report.filename = filename
                # Create upload directory if it doesn't exist
                os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
                report.filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                # Save file and create report
                file.save(report.filepath)
            else:
                flash('File type not allowed. Please upload a valid file.')
        db.session.add(report)
        db.session.commit()
        flash('Your report has been uploaded!')
        return redirect(url_for('main.reports'))
    return render_template('main/upload.html', title='Upload Report', form=form)

@bp.route('/reports')
@login_required
def reports():
    user_reports = current_user.reports.order_by(Report.timestamp.desc()).all()
    return render_template('main/reports.html', title='My Reports', reports=user_reports)